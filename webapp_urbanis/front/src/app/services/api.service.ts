import { Injectable } from '@angular/core';
import { environment} from '../../environments/environment';
import {HttpClient} from '@angular/common/http';
import {Search} from '../models/Search';
import {Sujet} from '../models/Sujet';
import {Observable, throwError} from 'rxjs';
import {catchError, map} from 'rxjs/operators';
import {Variable} from '../models/Variable';
import {Text} from '../models/Text';



const API_URL = environment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) {
  }

  public getSujets(): Observable<Sujet[]> {

    return this.httpClient.get(API_URL + '/sujets')
      .pipe(map((response: any) => {
        return response.map((sujet) => new Sujet(sujet));
      }), catchError(this.handleError));
  }


  public getVariables(): Observable<Variable[]>  {
    return this.httpClient.get(API_URL + '/variables')
      .pipe(map((response: any) => {
        return response.map((variable) => new Variable(variable));
      }), catchError(this.handleError));
  }

  public doSearch(search: Search): Observable<Text[]>  {
    return this.httpClient.post(API_URL + '/search', search)
      .pipe(map((response: any) => {
        return response.map((text) => new Text(text));
      }), catchError(this.handleError));
  }

  public handleError(error, caught) {
    console.error('ApiService:handleError', error);
    return throwError(error);
  }
}
