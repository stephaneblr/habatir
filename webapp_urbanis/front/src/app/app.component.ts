import {Component, ElementRef, ViewChild} from '@angular/core';
import {FormControl} from '@angular/forms';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';
import {ApiService} from './services/api.service';
import {Sujet} from './models/Sujet';
import {Variable} from './models/Variable';
import {Search} from './models/Search';
import {Text} from './models/Text';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import {MatAutocompleteSelectedEvent, MatChipInputEvent, MatSelectChange} from '@angular/material';
import {Regle} from './models/Regle';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';

  myControlSujets = new FormControl();
  filteredOptionsSujets: Observable<Sujet[]>;

  visible = true;
  selectable = true;
  removable = true;
  addOnBlur = false;
  separatorKeysCodes: number[] = [ENTER, COMMA];
  myControlVariables = new FormControl();
  filteredOptionsVariables: Observable<Variable[]>;
  variablesSelected = [];

  numberResultatFound = 0;


  @ViewChild('variableInput') variableInput: ElementRef;

  sujets: Sujet[];
  variabes: Variable[];
  texts: Text[];
  search: Search;
  regles: Regle[];
  constructor(private apiService: ApiService) {
    this.search = new Search();
    this.search.c1 = 0;
    this.search.c2 = [];
    this.sujets = [];
    this.variabes = [];
    this.texts = [];
    this.regles = [];
    this.regles.push(new Regle({
      id: 1,
      nom: 'contraignent'
    }), new Regle({
      id: 2,
      nom: 's\'appliquent en fonction de'
    }), new Regle({
      id: 3,
      nom: 'précisent la définition de'
    }) );
  }

  private addC2parameters() {
    this.search.c2 = [];
    for (let i = 0; i < this.variablesSelected.length; ++i) {
      if (this.variablesSelected[i].option) {
        this.search.c2.push({
          id: this.variablesSelected[i].id_variable,
          option: this.variablesSelected[i].option
        });
      }
    }
    console.log(this.search);
    this.doSearch(this.search);
  }


  private getCompletionSujet() {
    this.apiService.getSujets().subscribe((sujets) => {
      this.sujets = sujets;
      console.log(sujets);
    }, (error) => {
      console.log(error);
    });
  }

  private getCompletionVariables() {
    this.apiService.getVariables().subscribe((variables) => {
      this.variabes = variables;
      console.log(variables);
    }, (error) => {
      console.log(error);
    });
  }

  private doSearch(search: Search) {
    this.apiService.doSearch(search).subscribe((texts) => {
      this.texts = texts;
      this.numberResultatFound = this.texts.length;
      console.log(texts);
    }, (error) => {
      console.log(error);
    });
  }

  ngOnInit() {
    this.getCompletionSujet();
    this.getCompletionVariables();
    this.doSearch(this.search);
    this.filteredOptionsSujets = this.myControlSujets.valueChanges
      .pipe(
        startWith<string | Sujet>(''),
        map(value => typeof value === 'string' ? value : value.nom),
        map(nom => this._sujetsFilter(nom))
      );
    this.filteredOptionsVariables = this.myControlVariables.valueChanges
      .pipe(
        startWith<string | Variable>(''),
        map(value => typeof value === 'string' ? value : value.nom),
        map(nom => this._variableFilter(nom))
      );
  }

  add(event: MatChipInputEvent): void {

  }

  remove(variable: Variable): void {
    const index = this.variablesSelected.indexOf(variable);
    if (index >= 0) {
      this.variablesSelected[index].option = null;
      this.variablesSelected.splice(index, 1);
    }
    this.addC2parameters();
  }

  selectedVariable(event: MatAutocompleteSelectedEvent): void {
    const variableSelected: Variable = event.option.value;
    this.variablesSelected.push(variableSelected);
    this.variableInput.nativeElement.value = '';
    this.myControlVariables.setValue( '');
  }

  displayFn(sujet?: Sujet): string | undefined {
    return sujet ? sujet.nom : undefined;
  }

  sujetSelected(event) {
    const sujetSelected: Sujet = event.option.value;
    this.search.c1 = sujetSelected.id_sujet;
    console.log(this.search);
    this.doSearch(this.search);
  }


  private _variableFilter(value: string): Variable[] {
    const filterValue = value;
    if (!value) {
      return [];
    }
    return this.variabes.filter(variable => variable.nom.toLowerCase().includes(filterValue));
  }

  private _sujetsFilter(value: string): Sujet[] {
    const filterValue = value.toLowerCase();
    console.log(filterValue);
    if (!value) {
      return [];
    }
    return this.sujets.filter(sujet => sujet.nom.toLowerCase().includes(filterValue));
  }

  onSujetChange(value: string) {
    if (!value) {
      this.search.c1 = 0;
      this.doSearch(this.search);
    }
  }

  onRegleSelected(value: Regle, variable: Variable) {
    const index = this.variablesSelected.indexOf(variable);
    this.variablesSelected[index].option = value.id;
    this.addC2parameters();
  }

  onClickMe(row) {
    // console.log(text);
    this.texts[row].clicked = !this.texts[row].clicked;
  }
}
