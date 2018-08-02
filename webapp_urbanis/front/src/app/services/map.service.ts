import { Injectable } from '@angular/core';
import {environment} from '../../environments/environment';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

const mapToken = environment.mapboxToken;
const API_URL = environment.apiCartoGPUUrl;
const CADASTRE_KEY = environment.cadastreKey;

@Injectable({
  providedIn: 'root'
})
export class MapService {

  constructor(private httpClient: HttpClient) {
  }

  private getArg(lng, lat) {
    return {
      type: 'Point',
      coordinates: [lng, lat]
    };
  }

  public getDocument(lng, lat): Observable<any> {
    return this.httpClient.get(API_URL + '/gpu/document?geom=' + JSON.stringify(this.getArg(lng, lat)));
  }

  public getZoneUrba(lng, lat): Observable<any> {
    return this.httpClient.get(API_URL + '/gpu/zone-urba?geom=' + JSON.stringify(this.getArg(lng, lat)));
  }

  public getCommune(lng, lat): Observable<any> {
    return this.httpClient.get(API_URL + '/cadastre/commune?geom=' + JSON.stringify(this.getArg(lng, lat) +
                              '&apiKey=' + CADASTRE_KEY));
  }

  public getParcelle(codeInsee): Observable<any> {
    return this.httpClient.get(API_URL + '/cadastre/parcelle?code_insee=' + codeInsee + '&apiKey=' + CADASTRE_KEY);
  }
}
