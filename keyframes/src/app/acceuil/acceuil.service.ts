import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AcceuilService {
  frameUrl='http://localhost:5000/api/video';
  upUrl='http://localhost:5000/api/upload';
  

  constructor(private http: HttpClient) { }

  getVideos(){
    return this.http.get<any>(this.frameUrl);
  }  

  upload(a:string){
    console.log(this.upUrl+'/'+a)
    return this.http.get<any>(this.upUrl+'/'+a)
  }
}
