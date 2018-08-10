export class Sujet {
  id_sujet: number;
  nom: string;

  constructor(values: Object = {}) {
    Object.assign(this, values);
  }
}
