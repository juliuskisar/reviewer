/**
 * review.js — interatividade offline para páginas de revisão estática.
 * Navegação por abas (cada aba = um painel/página) + quiz + progresso.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'review-progress';
  var PANELS_KEY = 'review-panels-visited';
  var data = window.REVIEW_DATA || { exercises: [] };

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); }

  function getExercise(id) {
    return (data.exercises || []).find(function (e) { return e.id === id; });
  }

  function normalizeWrittenText(text) {
    if (!text) return '';
    var s = String(text).trim().toLowerCase();
    s = s.replace(/[\u2018\u2019]/g, "'");
    s = s.replace(/\s+/g, ' ');
    s = s.replace(/[.!?;,]+$/, '');
    return s;
  }

  function levenshtein(a, b) {
    if (a === b) return 0;
    if (!a.length) return b.length;
    if (!b.length) return a.length;
    var row = [];
    var i, j;
    for (j = 0; j <= b.length; j++) row[j] = j;
    for (i = 1; i <= a.length; i++) {
      var prev = i;
      for (j = 1; j <= b.length; j++) {
        var val = a[i - 1] === b[j - 1] ? row[j - 1] : Math.min(row[j - 1], row[j], prev) + 1;
        row[j - 1] = prev;
        prev = val;
      }
      row[b.length] = prev;
    }
    return row[b.length];
  }

  function collectWrittenAccepted(exercise) {
    var list = [exercise.correct_answer];
    (exercise.accepted_answers || []).forEach(function (a) {
      if (a && list.indexOf(a) === -1) list.push(a);
    });
    return list;
  }

  function findMistakeHint(exercise, rawAnswer) {
    var lower = (rawAnswer || '').toLowerCase();
    var hints = exercise.mistake_hints || [];
    for (var i = 0; i < hints.length; i++) {
      if (lower.indexOf(hints[i].contains.toLowerCase()) !== -1) {
        return hints[i].message;
      }
    }
    return '';
  }

  function bestWrittenMatch(normalizedUser, acceptedNormalized) {
    var best = { index: -1, distance: 9999 };
    for (var i = 0; i < acceptedNormalized.length; i++) {
      var d = levenshtein(normalizedUser, acceptedNormalized[i]);
      if (d < best.distance) {
        best = { index: i, distance: d };
      }
    }
    return best;
  }

  function checkWrittenLanguage(exercise, item, feedback) {
    var field = $('#answer-' + exercise.id, item);
    if (!field) return;
    var raw = field.value || '';
    if (!raw.trim()) {
      feedback.textContent = 'Digite sua resposta antes de verificar.';
      feedback.className = 'quiz-feedback is-neutral';
      return;
    }

    var accepted = collectWrittenAccepted(exercise);
    var acceptedNorm = accepted.map(normalizeWrittenText);
    var userNorm = normalizeWrittenText(raw);
    var exactIdx = acceptedNorm.indexOf(userNorm);

    if (exactIdx !== -1) {
      feedback.textContent = 'Correto! ' + (exercise.explanation || '');
      feedback.className = 'quiz-feedback is-correct';
      markPanelVisited(item.closest('.page-panel'));
      return;
    }

    var mode = exercise.input_mode || 'sentence';
    var match = bestWrittenMatch(userNorm, acceptedNorm);
    var refLen = acceptedNorm[match.index] ? acceptedNorm[match.index].length : userNorm.length;
    var maxTypos = mode === 'word'
      ? (refLen <= 4 ? 1 : refLen <= 8 ? 2 : 3)
      : Math.max(2, Math.floor(refLen * 0.08));

    if (match.index >= 0 && match.distance > 0 && match.distance <= maxTypos) {
      feedback.innerHTML =
        'Quase lá — pequeno erro de digitação. ' +
        '<span class="written-correction">Forma esperada: «' + escapeHtml(accepted[match.index]) + '».</span> ' +
        (exercise.explanation || '');
      feedback.className = 'quiz-feedback is-almost';
      markPanelVisited(item.closest('.page-panel'));
      return;
    }

    var hint = findMistakeHint(exercise, raw);
    var msg = 'Ainda não está correto.';
    if (hint) {
      msg += ' ' + hint;
    }
    msg += ' <span class="written-correction">Resposta modelo: «' +
      escapeHtml(exercise.correct_answer) + '».</span>';
    if (exercise.explanation) {
      msg += ' ' + exercise.explanation;
    }
    feedback.innerHTML = msg;
    feedback.className = 'quiz-feedback is-incorrect';
    markPanelVisited(item.closest('.page-panel'));
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function getVisitedPanels() {
    try {
      var raw = sessionStorage.getItem(PANELS_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) { return []; }
  }

  function saveVisitedPanel(panelId) {
    try {
      var visited = getVisitedPanels();
      if (visited.indexOf(panelId) === -1) {
        visited.push(panelId);
        sessionStorage.setItem(PANELS_KEY, JSON.stringify(visited));
      }
    } catch (e) { /* ignore */ }
  }

  function updateProgressBar() {
    var panels = $$('.page-panel');
    var visited = getVisitedPanels();
    var completed = panels.filter(function (p) {
      return visited.indexOf(p.id) !== -1 || p.dataset.completed === 'true';
    }).length;
    var total = panels.length || 1;
    var pct = Math.round((completed / total) * 100);
    var fill = $('#progress-fill');
    var label = $('#progress-percent');
    var status = $('#progress-status');
    if (fill) fill.style.width = pct + '%';
    if (label) label.textContent = String(pct);
    if (status) status.textContent = completed + ' de ' + total + ' seções visitadas';
  }

  function markPanelVisited(panelEl) {
    if (!panelEl || !panelEl.id) return;
    panelEl.dataset.completed = 'true';
    saveVisitedPanel(panelEl.id);
    updateProgressBar();
  }

  function activatePanel(panelId) {
    $$('.page-panel').forEach(function (panel) {
      var active = panel.id === panelId;
      panel.classList.toggle('is-active', active);
      if (active) {
        panel.removeAttribute('hidden');
        markPanelVisited(panel);
      } else {
        panel.setAttribute('hidden', '');
      }
    });
    $$('.nav-tab').forEach(function (tab) {
      var active = tab.dataset.panel === panelId;
      tab.classList.toggle('is-active', active);
      tab.setAttribute('aria-selected', active ? 'true' : 'false');
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function initPageTabs() {
    $$('.nav-tab').forEach(function (tab) {
      tab.addEventListener('click', function () {
        activatePanel(tab.dataset.panel);
      });
    });
    var first = $('.nav-tab.is-active');
    if (first) markPanelVisited(document.getElementById(first.dataset.panel));
  }

  function checkAnswer(exerciseId) {
    var exercise = getExercise(exerciseId);
    var item = $('#exercise-' + exerciseId);
    var feedback = $('#feedback-' + exerciseId);
    if (!exercise || !item || !feedback) return;

    if (exercise.type === 'written_language') {
      checkWrittenLanguage(exercise, item, feedback);
      return;
    }

    if (exercise.type === 'open_response') {
      feedback.textContent = 'Use o checklist para autoavaliar sua resposta. Respostas discursivas não são corrigidas automaticamente.';
      feedback.className = 'quiz-feedback is-neutral';
      markPanelVisited(item.closest('.page-panel'));
      return;
    }

    if (exercise.type === 'map_capital') {
      var mapEl = $('[data-component="brazil-map"]', item);
      var group = $('.brazil-map__state-group.is-selected, .brazil-map__merged-group.is-selected', mapEl);
      var input = $('.brazil-map__capital-input', mapEl);
      if (!group) {
        feedback.textContent = 'Clique em um estado no mapa antes de verificar.';
        feedback.className = 'quiz-feedback is-neutral';
        return;
      }
      if (!input || !input.value.trim()) {
        feedback.textContent = 'Digite o nome da capital no campo abaixo do mapa.';
        feedback.className = 'quiz-feedback is-neutral';
        return;
      }
      var expected = group.dataset.capital || '';
      var isCorrect = normalizeCapital(input.value) === normalizeCapital(expected);
      if (isCorrect) {
        feedback.textContent = 'Correto! A capital é ' + expected + '. ' + (exercise.explanation || '');
        feedback.className = 'quiz-feedback is-correct';
      } else {
        feedback.textContent = 'Ainda não. A capital correta é ' + expected + '. Tente outro estado ou revise na aba Mapas interativos.';
        feedback.className = 'quiz-feedback is-incorrect';
      }
      markPanelVisited(item.closest('.page-panel'));
      return;
    }

    var selected = $('input[name="' + exerciseId + '"]:checked', item);
    if (!selected) {
      feedback.textContent = 'Selecione uma opção antes de verificar.';
      feedback.className = 'quiz-feedback is-neutral';
      return;
    }

    var isCorrect = false;
    if (exercise.type === 'multiple_choice') {
      isCorrect = parseInt(selected.value, 10) === exercise.correct_answer;
    } else if (exercise.type === 'true_false') {
      isCorrect = (selected.value === 'true') === exercise.correct_answer;
    }

    if (isCorrect) {
      feedback.textContent = 'Correto! ' + (exercise.explanation || '');
      feedback.className = 'quiz-feedback is-correct';
    } else {
      feedback.textContent = 'Ainda não. Tente novamente ou veja a explicação.';
      feedback.className = 'quiz-feedback is-incorrect';
    }
    markPanelVisited(item.closest('.page-panel'));
  }

  function showAnswer(exerciseId) {
    var exercise = getExercise(exerciseId);
    var item = $('#exercise-' + exerciseId);
    var reveal = $('#answer-reveal-' + exerciseId);
    if (!reveal) return;

    if (exercise && exercise.type === 'map_capital' && item) {
      var mapEl = $('[data-component="brazil-map"]', item);
      var group = $('.brazil-map__state-group.is-selected, .brazil-map__merged-group.is-selected', mapEl);
      var span = $('.map-capital-reveal', reveal);
      if (span && group) {
        span.textContent = group.dataset.capital || '—';
      }
    }
    reveal.classList.remove('is-hidden');
  }

  function initTabs() {
    $$('[data-component="tabs"]').forEach(function (tabs) {
      $$('[role="tab"]', tabs).forEach(function (tab) {
        tab.addEventListener('click', function () {
          var panelId = tab.getAttribute('aria-controls');
          $$('[role="tab"]', tabs).forEach(function (t) {
            t.classList.remove('is-active');
            t.setAttribute('aria-selected', 'false');
          });
          $$('[role="tabpanel"]', tabs).forEach(function (p) {
            p.classList.add('is-hidden');
            p.classList.remove('is-active');
          });
          tab.classList.add('is-active');
          tab.setAttribute('aria-selected', 'true');
          var panel = document.getElementById(panelId);
          if (panel) {
            panel.classList.remove('is-hidden');
            panel.classList.add('is-active');
          }
        });
      });
    });
  }

  function initQuiz() {
    $$('.btn-check').forEach(function (btn) {
      btn.addEventListener('click', function () {
        checkAnswer(btn.dataset.exerciseId);
      });
    });
    $$('.btn-show-answer').forEach(function (btn) {
      btn.addEventListener('click', function () {
        showAnswer(btn.dataset.exerciseId);
      });
    });
  }

  function resetProgress() {
    try {
      sessionStorage.removeItem(PANELS_KEY);
      sessionStorage.removeItem(STORAGE_KEY);
    } catch (e) { /* ignore */ }
    $$('.page-panel').forEach(function (p) { delete p.dataset.completed; });
    $$('.quiz-feedback').forEach(function (f) { f.textContent = ''; f.className = 'quiz-feedback'; });
    $$('.quiz-answer').forEach(function (a) { a.classList.add('is-hidden'); });
    $$('input[type="radio"]').forEach(function (i) { i.checked = false; });
    $$('textarea').forEach(function (t) { t.value = ''; });
    $$('.written-input').forEach(function (t) { t.value = ''; });
    updateProgressBar();
  }

  function initRouteLinks() {
    $$('[data-goto-panel]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var panelId = btn.getAttribute('data-goto-panel');
        if (panelId) activatePanel(panelId);
      });
    });
  }

  function initReset() {
    var btn = $('#btn-reset-progress');
    if (btn) btn.addEventListener('click', resetProgress);
  }

  var MAP_DATA = window.BRAZIL_MAP_DATA || { periods: {}, modes: {} };

  function normalizeCapital(value) {
    return String(value || '')
      .trim()
      .toLowerCase()
      .normalize('NFD')
      .replace(/\p{M}/gu, '')
      .replace(/\s+/g, ' ');
  }

  var REGION_CLASS = {
    Norte: 'region-norte',
    Nordeste: 'region-nordeste',
    'Centro-Oeste': 'region-centro-oeste',
    Sudeste: 'region-sudeste',
    Sul: 'region-sul'
  };

  function applyMapPeriod(mapEl, period) {
    var cfg = MAP_DATA.periods[period] || {};
    var hidden = cfg.hidden_states || [];
    var visibleMerged = cfg.visible_merged || [];

    $$('.brazil-map__state-group', mapEl).forEach(function (group) {
      var id = group.dataset.state;
      group.classList.toggle('is-hidden', hidden.indexOf(id) !== -1);
    });

    var mergedLayer = $('.brazil-map__merged', mapEl);
    if (mergedLayer) {
      mergedLayer.classList.toggle('is-hidden', visibleMerged.length === 0);
      mergedLayer.setAttribute('aria-hidden', visibleMerged.length === 0 ? 'true' : 'false');
    }

    $$('.brazil-map__merged-group', mapEl).forEach(function (group) {
      var id = group.dataset.merged;
      var show = visibleMerged.indexOf(id) !== -1;
      group.classList.toggle('is-hidden', !show);
      group.setAttribute('aria-hidden', show ? 'false' : 'true');
    });

    $$('.brazil-map__label--merged', mapEl).forEach(function (label) {
      var forId = label.getAttribute('data-for');
      label.classList.toggle('is-hidden', visibleMerged.indexOf(forId) === -1);
    });

    $$('.brazil-map__period-btn', mapEl).forEach(function (btn) {
      btn.classList.toggle('is-active', btn.dataset.period === period);
    });
    mapEl.dataset.period = period;
    updateMapLabels(mapEl, mapEl.dataset.mode || 'evolution');
  }

  function updateMapLabels(mapEl, mode) {
    var labelsLayer = $('.brazil-map__labels', mapEl);
    if (labelsLayer) {
      labelsLayer.classList.toggle('is-hidden', mode !== 'capitals');
      labelsLayer.setAttribute('aria-hidden', mode !== 'capitals' ? 'true' : 'false');
    }
    $$('.brazil-map__label', mapEl).forEach(function (label) {
      var forId = label.getAttribute('data-for');
      var stateGroup = $('.brazil-map__state-group[data-state="' + forId + '"]', mapEl);
      var mergedGroup = $('.brazil-map__merged-group[data-merged="' + forId + '"]', mapEl);
      var hidden = (stateGroup && stateGroup.classList.contains('is-hidden')) ||
        (mergedGroup && mergedGroup.classList.contains('is-hidden'));
      label.classList.toggle('is-hidden', mode !== 'capitals' || hidden);
    });
  }

  var THEMATIC_MODES = ['imaginary_lines', 'climates', 'vegetation'];

  function themeFor(mode) {
    return (MAP_DATA.thematic || {})[mode] || null;
  }

  function legendItem(theme, id) {
    if (!theme) return null;
    for (var i = 0; i < theme.legend.length; i++) {
      if (theme.legend[i].id === id) return theme.legend[i];
    }
    return null;
  }

  function stateThemeIds(group, theme) {
    if (!theme) return [];
    var raw = group.dataset[theme.state_key === 'lines' ? 'zone' : theme.state_key] || '';
    return raw.split(',').filter(Boolean);
  }

  function renderMapLegend(mapEl, mode) {
    var legendEl = $('[data-legend]', mapEl);
    if (!legendEl) return;
    var theme = themeFor(mode);
    if (!theme) {
      legendEl.classList.add('is-hidden');
      legendEl.innerHTML = '';
      return;
    }
    var html = '<p class="brazil-map__legend-title">' + theme.title + '</p><ul class="brazil-map__legend-list">';
    theme.legend.forEach(function (item) {
      html += '<li class="brazil-map__legend-item">' +
        '<span class="brazil-map__legend-swatch" style="background:' + item.color + '"></span>' +
        '<span class="brazil-map__legend-label">' + item.label + '</span></li>';
    });
    html += '</ul>';
    if (theme.note) html += '<p class="brazil-map__legend-note">' + theme.note + '</p>';
    legendEl.innerHTML = html;
    legendEl.classList.remove('is-hidden');
  }

  function applyThemeFills(mapEl, mode) {
    var theme = themeFor(mode);
    $$('.brazil-map__state-group', mapEl).forEach(function (group) {
      if (!theme) {
        group.style.removeProperty('--theme-fill');
        return;
      }
      var ids = stateThemeIds(group, theme);
      var item = legendItem(theme, ids[0]);
      if (item) {
        group.style.setProperty('--theme-fill', item.color);
      } else {
        group.style.removeProperty('--theme-fill');
      }
    });
    var parallels = $('.brazil-map__parallels', mapEl);
    if (parallels) {
      var showLines = mode === 'imaginary_lines';
      parallels.classList.toggle('is-hidden', !showLines);
      parallels.setAttribute('aria-hidden', showLines ? 'false' : 'true');
    }
  }

  function applyMapMode(mapEl, mode) {
    var cfg = MAP_DATA.modes[mode] || {};
    var descEl = $('.brazil-map__mode-desc', mapEl);
    if (descEl) descEl.textContent = cfg.description || '';

    mapEl.dataset.mode = mode;
    Array.prototype.slice.call(mapEl.classList).forEach(function (cls) {
      if (cls.indexOf('brazil-map--mode-') === 0) mapEl.classList.remove(cls);
    });
    mapEl.classList.add('brazil-map--mode-' + mode);
    mapEl.classList.toggle('brazil-map--thematic', THEMATIC_MODES.indexOf(mode) !== -1);
    applyThemeFills(mapEl, mode);
    renderMapLegend(mapEl, mode);

    var panel = $('.brazil-map__panel', mapEl);
    var capitalQuiz = $('.brazil-map__capital-quiz', mapEl);
    var detail = $('.brazil-map__detail', mapEl);
    var hint = $('.brazil-map__hint', mapEl);
    if (mode === 'capital_quiz' || mode === 'capital_game') {
      if (panel) panel.classList.remove('is-hidden');
      if (capitalQuiz) capitalQuiz.classList.add('is-hidden');
      if (detail) detail.classList.add('is-hidden');
      if (hint) {
        hint.classList.remove('is-hidden');
        hint.textContent = mode === 'capital_game'
          ? 'Clique em um estado, digite a capital e clique em Confirmar.'
          : 'Clique em um estado e digite a capital no campo que vai aparecer.';
      }
    } else {
      if (capitalQuiz) capitalQuiz.classList.add('is-hidden');
      if (hint) hint.textContent = 'Clique em um estado para ver detalhes.';
    }

    $$('.brazil-map__mode-btn', mapEl).forEach(function (btn) {
      btn.classList.toggle('is-active', btn.dataset.mode === mode);
    });

    var periodsEl = $('.brazil-map__periods', mapEl);
    if (periodsEl) {
      periodsEl.classList.toggle('is-hidden', mode !== 'evolution');
    }

    $$('.brazil-map__state-group', mapEl).forEach(function (group) {
      group.classList.remove(
        'is-highlighted', 'region-norte', 'region-nordeste',
        'region-centro-oeste', 'region-sudeste', 'region-sul'
      );
      var region = group.dataset.region;
      var regionClass = REGION_CLASS[region];
      if (mode === 'regions' && regionClass) {
        group.classList.add(regionClass);
      }
      if (mode === 'new_states' && group.dataset.created) {
        group.classList.add('is-highlighted');
      }
    });

    updateMapLabels(mapEl, mode);

    if (mode === 'evolution') {
      applyMapPeriod(mapEl, mapEl.dataset.period || 'post_1988');
    } else {
      applyMapPeriod(mapEl, 'post_1988');
    }
  }

  function applyMapHighlight(mapEl, highlightIds) {
    if (mapEl.dataset.mode === 'new_states') return;
    $$('.brazil-map__state-group', mapEl).forEach(function (group) {
      group.classList.toggle('is-highlighted', highlightIds.indexOf(group.dataset.state) !== -1);
    });
  }

  function showMapDetail(mapEl, data) {
    var detail = $('.brazil-map__detail', mapEl);
    var hint = $('.brazil-map__hint', mapEl);
    if (!detail || !data) return;

    $('.brazil-map__detail-name', detail).textContent = data.name + (data.id ? ' (' + data.id + ')' : '');
    $('.brazil-map__detail-capital', detail).textContent = data.capital || '';
    $('.brazil-map__detail-region', detail).textContent = data.region || '';

    var themeEl = $('.brazil-map__detail-theme', detail);
    if (themeEl) {
      if (data.themeHtml) {
        themeEl.innerHTML = data.themeHtml;
        themeEl.classList.remove('is-hidden');
      } else {
        themeEl.innerHTML = '';
        themeEl.classList.add('is-hidden');
      }
    }

    var noteEl = $('.brazil-map__detail-note', detail);
    noteEl.textContent = data.note || '';

    if (hint) hint.classList.add('is-hidden');
    detail.classList.remove('is-hidden');
  }

  function showCapitalQuizInput(mapEl, group) {
    var capitalQuiz = $('.brazil-map__capital-quiz', mapEl);
    var detail = $('.brazil-map__detail', mapEl);
    var hint = $('.brazil-map__hint', mapEl);
    var labelText = $('.brazil-map__capital-label-text', mapEl);
    var gameStateName = $('.brazil-map__game-state-name', mapEl);
    var input = $('.brazil-map__capital-input', mapEl);
    var feedback = $('.brazil-map__capital-feedback', mapEl);
    if (!capitalQuiz || !group) return;

    var name = group.dataset.name || group.dataset.state || group.dataset.merged;
    var id = group.dataset.state || group.dataset.merged || '';
    if (mapEl.dataset.mode === 'capital_game') {
      if (gameStateName) gameStateName.textContent = name + (id ? ' (' + id + ')' : '');
    } else if (labelText) {
      labelText.textContent = 'Qual é a capital de ' + name + (id ? ' (' + id + ')' : '') + '?';
    }
    if (feedback) feedback.textContent = '';
    if (input) {
      input.value = '';
      input.focus();
    }
    if (hint) hint.classList.add('is-hidden');
    if (detail) detail.classList.add('is-hidden');
    capitalQuiz.classList.remove('is-hidden');
  }

  function showMapStateDetail(mapEl, group) {
    if (mapEl.dataset.mode === 'capital_quiz' || mapEl.dataset.mode === 'capital_game') {
      showCapitalQuizInput(mapEl, group);
      return;
    }
    var period = mapEl.dataset.period || 'post_1988';
    var isMerged = group.classList.contains('brazil-map__merged-group');
    var note = group.dataset.note || '';
    var created = group.dataset.created;

    if (!isMerged && created && mapEl.dataset.mode === 'evolution') {
      note = 'Estado criado em ' + created + '.';
    }
    if (!note && isMerged) {
      note = group.dataset.note || '';
    }

    var themeHtml = '';
    var theme = themeFor(mapEl.dataset.mode);
    if (theme && !isMerged) {
      themeHtml = buildThemeDetail(group, theme, mapEl.dataset.mode);
    }

    showMapDetail(mapEl, {
      name: group.dataset.name || group.dataset.state || group.dataset.merged,
      id: group.dataset.state || group.dataset.merged,
      capital: group.dataset.capital,
      region: group.dataset.region,
      note: note,
      themeHtml: themeHtml
    });
  }

  function buildThemeDetail(group, theme, mode) {
    var ids = stateThemeIds(group, theme);
    if (!ids.length) return '';
    var html = '<p class="brazil-map__theme-title">' + theme.title + '</p>';
    if (mode === 'imaginary_lines') {
      var item = legendItem(theme, ids[0]);
      var cuts = [];
      if (group.dataset.cutEquator === 'true') cuts.push('linha do Equador');
      if (group.dataset.cutCapricorn === 'true') cuts.push('Trópico de Capricórnio');
      html += '<p class="brazil-map__theme-main"><span class="brazil-map__legend-swatch" style="background:' +
        (item ? item.color : '#ccc') + '"></span>' + (item ? item.label : '') + '</p>';
      html += '<p class="brazil-map__theme-desc">' + (item ? item.description : '') + '</p>';
      html += '<p class="brazil-map__theme-desc">' + (cuts.length
        ? 'Cortado por: ' + cuts.join(' e ') + '.'
        : 'Nenhuma das duas linhas passa por este estado.') + '</p>';
      return html;
    }
    ids.forEach(function (id, idx) {
      var li = legendItem(theme, id);
      if (!li) return;
      html += '<p class="' + (idx === 0 ? 'brazil-map__theme-main' : 'brazil-map__theme-other') + '">' +
        '<span class="brazil-map__legend-swatch" style="background:' + li.color + '"></span>' +
        li.label + (idx === 0 ? ' <small>(predominante)</small>' : '') + '</p>';
      if (idx === 0) html += '<p class="brazil-map__theme-desc">' + li.description + '</p>';
    });
    if (ids.length > 1) {
      html += '<p class="brazil-map__theme-desc"><em>Também ocorre no estado: ' +
        ids.slice(1).map(function (id) { var li = legendItem(theme, id); return li ? li.label : id; }).join(', ') +
        '.</em></p>';
    }
    return html;
  }

  function selectMapGroup(mapEl, group) {
    $$('.brazil-map__state-group, .brazil-map__merged-group', mapEl).forEach(function (g) {
      g.classList.toggle('is-selected', g === group);
    });
    showMapStateDetail(mapEl, group);
  }

  function initCapitalGame() {
    $$('[data-component="capital-game"]').forEach(function (gameRoot) {
      var mapEl = $('[data-component="brazil-map"]', gameRoot);
      if (!mapEl) return;

      var total = (MAP_DATA.states || []).length || 27;
      var scoreEl = $('.capital-game__score', gameRoot);
      var timerEl = $('.capital-game__timer', gameRoot);
      var victoryEl = $('.capital-game__victory', gameRoot);
      var victoryText = $('.capital-game__victory-text', gameRoot);
      var resetBtn = $('.capital-game__reset', gameRoot);
      var submitBtn = $('.brazil-map__capital-submit', mapEl);
      var startTime = null;
      var timerInterval = null;
      var selectedGroup = null;
      var defaultHint = ($('.brazil-map__hint', mapEl) || {}).textContent || 'Clique em um estado para ver detalhes.';

      function formatTime(ms) {
        var sec = Math.floor(ms / 1000);
        var min = Math.floor(sec / 60);
        sec = sec % 60;
        return String(min).padStart(2, '0') + ':' + String(sec).padStart(2, '0');
      }

      function countCompleted() {
        return $$('.brazil-map__state-group.is-completed', mapEl).length;
      }

      function updateScore() {
        if (scoreEl) scoreEl.textContent = countCompleted() + ' / ' + total;
      }

      function startTimer() {
        if (startTime) return;
        startTime = Date.now();
        timerInterval = setInterval(function () {
          if (timerEl) timerEl.textContent = formatTime(Date.now() - startTime);
        }, 1000);
      }

      function stopTimer() {
        if (timerInterval) {
          clearInterval(timerInterval);
          timerInterval = null;
        }
      }

      function hideQuizPanel() {
        var capitalQuiz = $('.brazil-map__capital-quiz', mapEl);
        var hint = $('.brazil-map__hint', mapEl);
        if (capitalQuiz) capitalQuiz.classList.add('is-hidden');
        if (hint) hint.classList.remove('is-hidden');
        selectedGroup = null;
        $$('.brazil-map__state-group', mapEl).forEach(function (g) {
          g.classList.remove('is-selected');
        });
      }

      function checkVictory() {
        var done = countCompleted();
        if (done < total) return;
        stopTimer();
        var elapsed = startTime ? Date.now() - startTime : 0;
        if (victoryText) {
          victoryText.textContent = 'Você completou todas as ' + total + ' capitais em ' +
            formatTime(elapsed) + '!';
        }
        if (victoryEl) victoryEl.classList.remove('is-hidden');
        hideQuizPanel();
      }

      function resetGame() {
        stopTimer();
        startTime = null;
        if (timerEl) timerEl.textContent = '00:00';
        updateScore();
        if (victoryEl) victoryEl.classList.add('is-hidden');
        $$('.brazil-map__state-group', mapEl).forEach(function (g) {
          g.classList.remove('is-completed', 'is-selected');
        });
        hideQuizPanel();
        var hint = $('.brazil-map__hint', mapEl);
        if (hint) hint.textContent = defaultHint;
        var feedback = $('.brazil-map__capital-feedback', mapEl);
        if (feedback) feedback.textContent = '';
      }

      function confirmAnswer() {
        if (!selectedGroup) return;
        startTimer();
        var input = $('.brazil-map__capital-input', mapEl);
        var feedback = $('.brazil-map__capital-feedback', mapEl);
        if (!input || !input.value.trim()) {
          if (feedback) feedback.textContent = 'Digite o nome da capital.';
          return;
        }
        var expected = selectedGroup.dataset.capital || '';
        if (normalizeCapital(input.value) === normalizeCapital(expected)) {
          selectedGroup.classList.add('is-completed');
          selectedGroup.classList.remove('is-selected');
          if (feedback) feedback.textContent = 'Correto!';
          updateScore();
          setTimeout(function () { hideQuizPanel(); checkVictory(); }, 600);
        } else {
          if (feedback) feedback.textContent = 'Ainda não. Tente novamente!';
        }
      }

      applyMapMode(mapEl, 'capital_game');

      $$('.brazil-map__state', mapEl).forEach(function (path) {
        function activate() {
          var group = path.closest('.brazil-map__state-group');
          if (!group || group.classList.contains('is-hidden')) return;
          if (group.classList.contains('is-completed')) {
            var hint = $('.brazil-map__hint', mapEl);
            if (hint) {
              hint.textContent = 'Este estado já foi completado! Escolha outro.';
              hint.classList.remove('is-hidden');
            }
            $('.brazil-map__capital-quiz', mapEl).classList.add('is-hidden');
            return;
          }
          selectedGroup = group;
          $$('.brazil-map__state-group', mapEl).forEach(function (g) {
            g.classList.toggle('is-selected', g === group);
          });
          showCapitalQuizInput(mapEl, group);
        }
        path.addEventListener('click', activate);
        path.addEventListener('keydown', function (e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            activate();
          }
        });
      });

      if (submitBtn) submitBtn.addEventListener('click', confirmAnswer);
      var input = $('.brazil-map__capital-input', mapEl);
      if (input) {
        input.addEventListener('keydown', function (e) {
          if (e.key === 'Enter') {
            e.preventDefault();
            confirmAnswer();
          }
        });
      }
      if (resetBtn) resetBtn.addEventListener('click', resetGame);
      updateScore();
    });
  }

  function initBrazilMaps() {
    $$('[data-component="brazil-map"]').forEach(function (mapEl) {
      if (mapEl.closest('[data-component="capital-game"]')) return;
      if (mapEl.closest('[data-component="map-theme-game"]')) return;
      var period = mapEl.dataset.period || 'post_1988';
      var mode = mapEl.dataset.mode || 'evolution';
      var highlight = (mapEl.dataset.highlight || '').split(',').filter(Boolean);
      var interactive = mapEl.dataset.interactive !== 'false';

      applyMapMode(mapEl, mode);
      if (highlight.length) applyMapHighlight(mapEl, highlight);

      $$('.brazil-map__period-btn', mapEl).forEach(function (btn) {
        btn.addEventListener('click', function () {
          applyMapPeriod(mapEl, btn.dataset.period);
          var selected = $('.brazil-map__state-group.is-selected, .brazil-map__merged-group.is-selected', mapEl);
          if (selected) showMapStateDetail(mapEl, selected);
        });
      });

      $$('.brazil-map__mode-btn', mapEl).forEach(function (btn) {
        btn.addEventListener('click', function () {
          applyMapMode(mapEl, btn.dataset.mode);
          $$('.brazil-map__state-group, .brazil-map__merged-group', mapEl).forEach(function (g) {
            g.classList.remove('is-selected');
          });
          var detail = $('.brazil-map__detail', mapEl);
          var hint = $('.brazil-map__hint', mapEl);
          if (detail) detail.classList.add('is-hidden');
          if (hint) hint.classList.remove('is-hidden');
        });
      });

      if (!interactive) return;

      $$('.brazil-map__state', mapEl).forEach(function (path) {
        function activate() {
          var group = path.closest('.brazil-map__state-group, .brazil-map__merged-group');
          if (group && !group.classList.contains('is-hidden')) selectMapGroup(mapEl, group);
        }
        path.addEventListener('click', activate);
        path.addEventListener('keydown', function (e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            activate();
          }
        });
      });
    });
  }

  var GLOBE_ZONES = (function () {
    var out = {};
    var zones = (window.THERMAL_GLOBE_DATA || {}).zones || [];
    zones.forEach(function (z) { out[z.id] = z; });
    return out;
  })();

  function initThermalGlobes() {
    $$('[data-component="thermal-globe"]').forEach(function (root) {
      var palette = $('.thermal-globe__palette', root);
      var hint = $('.thermal-globe__hint', root);
      var detail = $('.thermal-globe__detail', root);
      var nameEl = $('.thermal-globe__detail-name', root);
      var raysEl = $('.thermal-globe__detail-rays', root);
      var tempEl = $('.thermal-globe__detail-temp', root);
      var feedback = $('.thermal-globe__feedback', root);
      var bands = $$('.thermal-globe__band', root);
      var lines = $$('.thermal-globe__parallel', root);
      var chosenZone = null;

      function setMode(mode) {
        root.dataset.mode = mode;
        root.classList.toggle('thermal-globe--paint', mode === 'paint');
        root.classList.toggle('thermal-globe--explore', mode !== 'paint');
        if (palette) palette.classList.toggle('is-hidden', mode !== 'paint');
        $$('.thermal-globe__mode-btn', root).forEach(function (btn) {
          btn.classList.toggle('is-active', btn.dataset.mode === mode);
        });
        if (detail) detail.classList.add('is-hidden');
        if (feedback) feedback.textContent = '';
        if (hint) {
          hint.classList.remove('is-hidden');
          hint.textContent = mode === 'paint'
            ? 'Escolha uma cor, clique nas faixas do globo e depois em Verificar.'
            : 'Clique em uma faixa ou em uma linha para ver a explicação.';
        }
        bands.forEach(function (band) {
          band.classList.remove('is-right', 'is-wrong', 'is-selected');
          band.style.removeProperty('--painted');
          band.removeAttribute('data-painted');
        });
      }

      function showBand(band) {
        var zone = GLOBE_ZONES[band.dataset.zone] || {};
        if (nameEl) nameEl.textContent = band.dataset.label || zone.label || '';
        if (raysEl) raysEl.textContent = zone.rays || '';
        if (tempEl) tempEl.textContent = zone.temperature || '';
        if (hint) hint.classList.add('is-hidden');
        if (detail) detail.classList.remove('is-hidden');
        bands.forEach(function (b) { b.classList.toggle('is-selected', b === band); });
      }

      function showLine(line) {
        var texts = {
          equator: 'Paralelo 0°: divide a Terra em hemisfério Norte e hemisfério Sul. É onde o Sol incide mais perpendicularmente.',
          cancer: 'Limite norte da zona intertropical — até aqui os raios solares chegam perpendiculares.',
          capricorn: 'Limite sul da zona intertropical. Passa pelo Brasil (MS, SP e PR).',
          arctic: 'Limite da zona polar Norte — raios muito inclinados; sol da meia-noite no verão.',
          antarctic: 'Limite da zona polar Sul — raios muito inclinados; noite longa no inverno.'
        };
        if (nameEl) nameEl.textContent = line.dataset.label || '';
        if (raysEl) raysEl.textContent = texts[line.dataset.parallel] || '';
        if (tempEl) tempEl.textContent = '';
        if (hint) hint.classList.add('is-hidden');
        if (detail) detail.classList.remove('is-hidden');
        bands.forEach(function (b) { b.classList.remove('is-selected'); });
      }

      function paintBand(band) {
        if (!chosenZone) {
          if (feedback) feedback.textContent = 'Primeiro escolha uma cor na paleta.';
          return;
        }
        var zone = GLOBE_ZONES[chosenZone];
        band.style.setProperty('--painted', zone ? zone.color : '#ccc');
        band.setAttribute('data-painted', chosenZone);
        band.classList.remove('is-right', 'is-wrong');
        if (feedback) feedback.textContent = '';
      }

      function checkPaint() {
        var right = 0;
        var painted = 0;
        bands.forEach(function (band) {
          var chosen = band.getAttribute('data-painted');
          if (!chosen) {
            band.classList.remove('is-right', 'is-wrong');
            return;
          }
          painted += 1;
          var ok = chosen === band.dataset.zone;
          band.classList.toggle('is-right', ok);
          band.classList.toggle('is-wrong', !ok);
          if (ok) right += 1;
        });
        if (!feedback) return;
        if (painted < bands.length) {
          feedback.textContent = 'Faltam ' + (bands.length - painted) + ' faixa(s) para pintar.';
        } else if (right === bands.length) {
          feedback.textContent = 'Perfeito! Vermelho entre os trópicos, amarelo nas zonas temperadas e cinza nas polares.';
        } else {
          feedback.textContent = right + ' de ' + bands.length + ' faixas certas. Lembre: quanto mais perto dos polos, mais frio.';
        }
      }

      bands.forEach(function (band) {
        function activate() {
          if (root.dataset.mode === 'paint') paintBand(band); else showBand(band);
        }
        band.addEventListener('click', activate);
        band.addEventListener('keydown', function (e) {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); }
        });
      });

      lines.forEach(function (line) {
        function activate() {
          if (root.dataset.mode !== 'paint') showLine(line);
        }
        line.addEventListener('click', activate);
        line.addEventListener('keydown', function (e) {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); }
        });
      });

      $$('.thermal-globe__color-btn', root).forEach(function (btn) {
        btn.addEventListener('click', function () {
          chosenZone = btn.dataset.zone;
          $$('.thermal-globe__color-btn', root).forEach(function (b) { b.classList.toggle('is-active', b === btn); });
          if (feedback) feedback.textContent = '';
        });
      });

      var checkBtn = $('.thermal-globe__check', root);
      if (checkBtn) checkBtn.addEventListener('click', checkPaint);
      var resetBtn = $('.thermal-globe__reset', root);
      if (resetBtn) resetBtn.addEventListener('click', function () { setMode('paint'); });

      $$('.thermal-globe__mode-btn', root).forEach(function (btn) {
        btn.addEventListener('click', function () { setMode(btn.dataset.mode); });
      });

      setMode(root.dataset.mode || 'explore');
    });
  }

  function shuffleArray(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }

  function initMapThemeGames() {
    $$('[data-component="map-theme-game"]').forEach(function (gameRoot) {
      var mapEl = $('[data-component="brazil-map"]', gameRoot);
      var themeId = gameRoot.dataset.theme;
      var theme = themeFor(themeId);
      if (!mapEl || !theme) return;

      var scoreEl = $('.capital-game__score', gameRoot);
      var timerEl = $('.capital-game__timer', gameRoot);
      var errorsEl = $('.map-theme-game__errors', gameRoot);
      var questionEl = $('.map-theme-game__question', gameRoot);
      var optionsEl = $('.map-theme-game__options', gameRoot);
      var feedbackEl = $('.map-theme-game__feedback', gameRoot);
      var victoryEl = $('.capital-game__victory', gameRoot);
      var victoryText = $('.capital-game__victory-text', gameRoot);
      var resetBtn = $('.capital-game__reset', gameRoot);
      var groups = $$('.brazil-map__state-group', mapEl);
      var total = groups.length;
      var queue = [];
      var current = null;
      var correct = 0;
      var errors = 0;
      var startTime = null;
      var timerInterval = null;

      function formatTime(ms) {
        var sec = Math.floor(ms / 1000);
        var min = Math.floor(sec / 60);
        sec = sec % 60;
        return String(min).padStart(2, '0') + ':' + String(sec).padStart(2, '0');
      }
      function startTimer() {
        if (startTime) return;
        startTime = Date.now();
        timerInterval = setInterval(function () {
          if (timerEl) timerEl.textContent = formatTime(Date.now() - startTime);
        }, 1000);
      }
      function stopTimer() {
        if (timerInterval) { clearInterval(timerInterval); timerInterval = null; }
      }
      function updateScore() {
        if (scoreEl) scoreEl.textContent = correct + ' / ' + total;
        if (errorsEl) errorsEl.textContent = String(errors);
      }

      function renderOptions() {
        if (!optionsEl) return;
        optionsEl.innerHTML = '';
        theme.legend.forEach(function (item) {
          var btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'map-theme-game__option';
          btn.dataset.answer = item.id;
          btn.innerHTML = '<span class="brazil-map__legend-swatch" style="background:' + item.color + '"></span>' + item.label;
          btn.addEventListener('click', function () { answer(item.id, btn); });
          optionsEl.appendChild(btn);
        });
      }

      function nextQuestion() {
        groups.forEach(function (g) { g.classList.remove('is-selected'); });
        if (!queue.length) {
          current = null;
          finish();
          return;
        }
        current = queue.shift();
        current.classList.add('is-selected');
        if (questionEl) {
          questionEl.textContent = gameRoot.dataset.questionPrefix + ' ' +
            current.dataset.name + ' (' + current.dataset.state + ')?';
        }
        if (feedbackEl) feedbackEl.textContent = '';
        $$('.map-theme-game__option', gameRoot).forEach(function (b) { b.classList.remove('is-wrong'); b.disabled = false; });
      }

      function answer(id, btn) {
        if (!current) return;
        startTimer();
        var ids = stateThemeIds(current, theme);
        if (id === ids[0]) {
          var item = legendItem(theme, id);
          current.style.setProperty('--theme-fill', item ? item.color : '#ccc');
          current.classList.add('is-completed-theme');
          correct += 1;
          if (feedbackEl) {
            var extra = ids.length > 1
              ? ' Também ocorre: ' + ids.slice(1).map(function (x) { var li = legendItem(theme, x); return li ? li.label : x; }).join(', ') + '.'
              : '';
            feedbackEl.textContent = 'Certo! ' + (item ? item.label : '') + ' predomina em ' + current.dataset.name + '.' + extra;
          }
          updateScore();
          setTimeout(nextQuestion, 900);
        } else {
          errors += 1;
          if (btn) { btn.classList.add('is-wrong'); btn.disabled = true; }
          if (feedbackEl) feedbackEl.textContent = 'Ainda não. Pense na região e no clima dela — tente outra opção.';
          updateScore();
        }
      }

      function finish() {
        stopTimer();
        var elapsed = startTime ? Date.now() - startTime : 0;
        if (questionEl) questionEl.textContent = 'Mapa completo!';
        if (victoryText) {
          victoryText.textContent = 'Você completou os ' + total + ' estados em ' + formatTime(elapsed) +
            ' com ' + errors + ' erro(s).';
        }
        if (victoryEl) victoryEl.classList.remove('is-hidden');
      }

      function resetGame() {
        stopTimer();
        startTime = null;
        correct = 0;
        errors = 0;
        if (timerEl) timerEl.textContent = '00:00';
        if (victoryEl) victoryEl.classList.add('is-hidden');
        groups.forEach(function (g) {
          g.classList.remove('is-completed-theme', 'is-selected');
          g.style.removeProperty('--theme-fill');
        });
        queue = shuffleArray(groups);
        updateScore();
        nextQuestion();
      }

      applyMapMode(mapEl, 'theme_game');
      mapEl.classList.add('brazil-map--thematic');
      renderMapLegend(mapEl, themeId);
      renderOptions();
      if (resetBtn) resetBtn.addEventListener('click', resetGame);
      resetGame();
    });
  }

  function initStudyGames() {
    $$('[data-component="study-game"]').forEach(function (root) {
      var mode = root.dataset.mode;
      var scoreEl = $('.study-game__score', root);
      var feedbackEl = $('.study-game__feedback', root);
      var victoryEl = $('.study-game__victory', root);
      var victoryText = $('.study-game__victory-text', root);
      var resetBtn = $('.study-game__reset', root);
      var total = 0;
      var correct = 0;

      function updateScore() {
        if (scoreEl) scoreEl.textContent = correct + ' / ' + total;
        if (correct === total && total > 0) {
          if (victoryEl) victoryEl.classList.remove('is-hidden');
          if (victoryText) victoryText.textContent = 'Você acertou todos! Boa revisão.';
        }
      }

      function resetGame() {
        correct = 0;
        if (feedbackEl) feedbackEl.textContent = '';
        if (victoryEl) victoryEl.classList.add('is-hidden');
        if (mode === 'sort_buckets') {
          $$('.study-game__chip', root).forEach(function (chip) {
            chip.classList.remove('is-correct', 'is-wrong', 'is-selected');
            chip.disabled = false;
            var pool = $('.study-game__items', root);
            if (pool) pool.appendChild(chip);
          });
          $$('.study-game__bucket-drop', root).forEach(function (drop) {
            drop.innerHTML = '';
          });
        } else if (mode === 'match_pairs') {
          $$('.study-game__match-card', root).forEach(function (card) {
            card.classList.remove('is-correct', 'is-wrong', 'is-selected');
            card.disabled = false;
          });
        }
        updateScore();
      }

      if (mode === 'sort_buckets') {
        var chips = $$('.study-game__chip', root);
        total = chips.length;
        var selectedChip = null;

        chips.forEach(function (chip) {
          chip.addEventListener('click', function () {
            if (chip.classList.contains('is-correct')) return;
            $$('.study-game__chip', root).forEach(function (c) { c.classList.remove('is-selected'); });
            chip.classList.add('is-selected');
            selectedChip = chip;
          });
        });

        $$('.study-game__bucket-drop', root).forEach(function (drop) {
          drop.addEventListener('click', function () {
            if (!selectedChip || selectedChip.classList.contains('is-correct')) return;
            var bucketId = drop.closest('.study-game__bucket').dataset.bucketId;
            var answer = selectedChip.dataset.answer;
            if (bucketId === answer) {
              selectedChip.classList.remove('is-selected', 'is-wrong');
              selectedChip.classList.add('is-correct');
              selectedChip.disabled = true;
              drop.appendChild(selectedChip);
              correct += 1;
              if (feedbackEl) feedbackEl.textContent = 'Certo!';
            } else {
              selectedChip.classList.add('is-wrong');
              if (feedbackEl) feedbackEl.textContent = 'Ops — tente outra categoria.';
              setTimeout(function () { selectedChip.classList.remove('is-wrong'); }, 600);
            }
            selectedChip = null;
            $$('.study-game__chip', root).forEach(function (c) { c.classList.remove('is-selected'); });
            updateScore();
          });
        });
      } else if (mode === 'match_pairs') {
        var leftCards = $$('.study-game__match-card--left', root);
        total = leftCards.length;
        var selectedLeft = null;

        leftCards.forEach(function (card) {
          card.addEventListener('click', function () {
            if (card.classList.contains('is-correct')) return;
            $$('.study-game__match-card--left', root).forEach(function (c) { c.classList.remove('is-selected'); });
            card.classList.add('is-selected');
            selectedLeft = card;
          });
        });

        $$('.study-game__match-card--right', root).forEach(function (card) {
          card.addEventListener('click', function () {
            if (!selectedLeft || card.classList.contains('is-correct')) return;
            if (selectedLeft.dataset.match === card.dataset.itemId) {
              selectedLeft.classList.remove('is-selected');
              selectedLeft.classList.add('is-correct');
              card.classList.add('is-correct');
              selectedLeft.disabled = true;
              card.disabled = true;
              correct += 1;
              if (feedbackEl) feedbackEl.textContent = 'Par!';
            } else {
              card.classList.add('is-wrong');
              if (feedbackEl) feedbackEl.textContent = 'Não combina — tente de novo.';
              setTimeout(function () { card.classList.remove('is-wrong'); }, 600);
            }
            selectedLeft = null;
            $$('.study-game__match-card--left', root).forEach(function (c) { c.classList.remove('is-selected'); });
            updateScore();
          });
        });
      }

      if (resetBtn) resetBtn.addEventListener('click', resetGame);
      updateScore();
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initPageTabs();
    initRouteLinks();
    initTabs();
    initQuiz();
    initReset();
    initBrazilMaps();
    initCapitalGame();
    initMapThemeGames();
    initThermalGlobes();
    initStudyGames();
    updateProgressBar();
  });
})();
