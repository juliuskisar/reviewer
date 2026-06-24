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

  function applyMapMode(mapEl, mode) {
    var cfg = MAP_DATA.modes[mode] || {};
    var descEl = $('.brazil-map__mode-desc', mapEl);
    if (descEl) descEl.textContent = cfg.description || '';

    mapEl.dataset.mode = mode;
    mapEl.classList.remove('brazil-map--mode-evolution', 'brazil-map--mode-regions',
      'brazil-map--mode-capitals', 'brazil-map--mode-new_states', 'brazil-map--mode-capital_quiz',
      'brazil-map--mode-capital_game');
    mapEl.classList.add('brazil-map--mode-' + mode);

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

    showMapDetail(mapEl, {
      name: group.dataset.name || group.dataset.state || group.dataset.merged,
      id: group.dataset.state || group.dataset.merged,
      capital: group.dataset.capital,
      region: group.dataset.region,
      note: note
    });
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

  document.addEventListener('DOMContentLoaded', function () {
    initPageTabs();
    initRouteLinks();
    initTabs();
    initQuiz();
    initReset();
    initBrazilMaps();
    initCapitalGame();
    updateProgressBar();
  });
})();
