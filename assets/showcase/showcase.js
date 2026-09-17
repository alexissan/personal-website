const activateStage = (root, stageId) => {
  const controls = [...root.querySelectorAll('.stage-control[data-stage]')];
  const selected = controls.find(control => control.dataset.stage === stageId) || controls[0];
  if (!selected) return;
  root.dataset.activeStage = selected.dataset.stage;
  controls.forEach(control => {
    if (control === selected) control.setAttribute('aria-current', 'step');
    else control.removeAttribute('aria-current');
  });
  const status = root.querySelector('.showcase-status');
  if (status) status.textContent = selected.dataset.status;
};

document.querySelectorAll('.showcase-mosaic[data-showcase]').forEach(root => {
  const controls = [...root.querySelectorAll('.stage-control[data-stage]')];
  if (!controls.length) return;
  activateStage(root, root.dataset.activeStage || controls[0].dataset.stage);
  controls.forEach(control => {
    ['pointerenter', 'focus', 'click'].forEach(eventName => {
      control.addEventListener(eventName, () => activateStage(root, control.dataset.stage));
    });
  });
});
