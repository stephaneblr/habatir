import { Component, OnInit } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';
import {environment} from '../../environments/environment';
import {GeoJson} from '../models/map';
import {MapService} from '../services/map.service';


@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.css']
})
export class MapsComponent implements OnInit {

  map: mapboxgl.Map;
  style = 'mapbox://styles/mapbox/light-v9';
  lat = 48.8354158166799;
  lng = 2.23263696544448;
  message = 'hello world';
  nbRequestDoc = 0;
  nbRequestZone = 0;

  infoMaps = {
    du_type: 'NULL',
    libelle: 'NULL',
    datvalid: 'NULL',
    adresse: 'NULL',
    numero_parcelle: 'NULL',
    superficie: 'NULL'
  };
  loaded = false;

  marker;
  layer;

  legend = {
    layers: ['Document', 'zone-urba'],
    colors: ['#ff4081', '#3f51b5']
  };

  constructor(private apiCartoService: MapService) {
  }

  private getDocument(lng, lat) {
    this.apiCartoService.getDocument(lng, lat).subscribe(results => {
      this.getProperties(results, 'du_type');
      this.addLayer((++this.nbRequestDoc).toString() + '-doc', results, '#ff4081');
      console.log(results);
    }, (error) => {
      console.log(error);
    });
  }

  private getProperties(results, field) {
    const features = results.features;
    if (features.length > 0) {
      this.infoMaps[field] = features[0].properties[field];
    } else {
      this.infoMaps[field] = 'NULL';
    }
  }



  private getParcelle(lng, lat) {
    this.apiCartoService.getCommune(lng, lat).subscribe(results => {
      console.log(results);
      this.apiCartoService.getParcelle(results.features[0].property.code_insee).subscribe(results1 => {
        this.getProperties(results1, 'adresse');
        this.getProperties(results1, 'numero_parcelle');
        this.getProperties(results1, 'superficie');
      }, (error1 => {
        console.log(error1);
      }));
    }, (error) => {
        console.log(error);
    });
  }

  private getZoneUrba(lng, lat) {
    this.apiCartoService.getZoneUrba(lng, lat).subscribe(results => {
      console.log(results.features);
      this.getProperties(results, 'libelle');
      this.getProperties(results, 'datvalid');
      this.addLayer((++this.nbRequestZone).toString() + '-zone', results, '#3f51b5');
    }, (error) => {
      console.log(error);
    });
  }

  private initializeMap() {
    mapboxgl.accessToken = environment.mapboxToken;
    this.map = new mapboxgl.Map({
      container: 'mapbox',
      style: this.style,
      zoom: 11,
      center : [this.lng, this.lat]
    });

    this.map.addControl(new mapboxgl.NavigationControl());

    this.map.on('click', (event) => {
      const coordinates = [event.lngLat.lng, event.lngLat.lat];
      const newMarker   = new GeoJson(coordinates, { message: this.message });
      console.log(JSON.stringify(newMarker));
      if (this.marker) {
        this.marker.remove();
      }
      this.marker = new mapboxgl.Marker()
        .setLngLat([event.lngLat.lng, event.lngLat.lat])
        .addTo(this.map);
      this.getDocument(coordinates[0], coordinates[1]);
      this.getZoneUrba(coordinates[0], coordinates[1]);
      // this.getParcelle(coordinates[0], coordinates[1]);
    });

    this.map.on('load', () => {
      this.loaded = true;
    });
  }

  private addLayer(id , data, color) {
    if (this.nbRequestZone > 1) {
      this.map.removeLayer((this.nbRequestZone - 1).toString() + '-zone');
    } if (this.nbRequestDoc > 1) {
      this.map.removeLayer((this.nbRequestDoc - 1).toString() + '-doc');
    }
    this.map.addLayer({
      'id': id,
      'type': 'fill',
      'source': {
        'type': 'geojson',
        'data': data
      },
      'layout': {},
      'paint': {
        'fill-color': color,
        'fill-opacity': 0.3
      }
    });
  }

  ngOnInit() {
    this.initializeMap();

  }

}
