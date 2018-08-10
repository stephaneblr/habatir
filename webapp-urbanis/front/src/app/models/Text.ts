export class Text {
  description_loi: string;
  id_loi: number;
  id_txt: number;
  lien: string;
  txt: string;
  clicked = false;

  constructor(values: Object = {}) {
    Object.assign(this, values);
  }
}
