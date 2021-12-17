import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class KeyframesService {

  frameUrl='http://localhost:5000/api/frame';
  constructor(private http: HttpClient) { }


getFrames(){
  return this.http.get<any>(this.frameUrl);
}  
}

