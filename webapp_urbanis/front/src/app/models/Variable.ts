export class Variable {
  id_variable: number;
  nom: string;
  option: number;

  constructor(values: Object = {}) {
    Object.assign(this, values);
  }
}
