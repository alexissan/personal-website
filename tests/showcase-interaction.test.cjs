const assert = require('assert');
const fs = require('fs');
const vm = require('vm');

class Control {
  constructor(stage, status) {
    this.dataset = {stage, status};
    this.attributes = {};
    this.listeners = {};
  }
  setAttribute(name, value) { this.attributes[name] = value; }
  removeAttribute(name) { delete this.attributes[name]; }
  addEventListener(name, handler) { this.listeners[name] = handler; }
  emit(name) { this.listeners[name](); }
}

const controls = [
  new Control('request', 'Request received'),
  new Control('understood', 'Request understood'),
  new Control('documents', 'Documents prepared')
];
const status = {textContent: ''};
const root = {
  dataset: {},
  querySelectorAll: selector => selector === '.stage-control[data-stage]' ? controls : [],
  querySelector: selector => selector === '.showcase-status' ? status : null
};
const document = {
  querySelectorAll: selector => selector === '.showcase-mosaic[data-showcase]' ? [root] : []
};

const source = fs.readFileSync('assets/showcase/showcase.js', 'utf8');
vm.runInNewContext(source, {document});

assert.equal(root.dataset.activeStage, 'request');
assert.equal(controls[0].attributes['aria-current'], 'step');
assert.equal(status.textContent, 'Request received');

controls[1].emit('pointerenter');
assert.equal(root.dataset.activeStage, 'understood');
assert.equal(controls[1].attributes['aria-current'], 'step');
assert.equal(controls[0].attributes['aria-current'], undefined);

controls[2].emit('focus');
assert.equal(root.dataset.activeStage, 'documents');
assert.equal(status.textContent, 'Documents prepared');

controls[0].emit('click');
assert.equal(root.dataset.activeStage, 'request');
assert.equal(controls.filter(control => control.attributes['aria-current'] === 'step').length, 1);

console.log('showcase interactions passed');
