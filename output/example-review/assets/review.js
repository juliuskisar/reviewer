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
    var reveal = $('#answer-reveal-' + exerciseId);
    if (reveal) reveal.classList.remove('is-hidden');
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

  document.addEventListener('DOMContentLoaded', function () {
    initPageTabs();
    initRouteLinks();
    initTabs();
    initQuiz();
    initReset();
    updateProgressBar();
  });
})();
