import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AcceuilService } from './acceuil.service'
@Component({
  selector: 'app-acceuil',
  templateUrl: './acceuil.component.html',
  styleUrls: ['./acceuil.component.css']
})
export class AcceuilComponent implements OnInit {

  videos?:any[]
  selectedVideo=""
  nom=""
  isLoading=false;

  constructor(private service: AcceuilService,private router: Router) { }

  ngOnInit(): void {
    this.service.getVideos().subscribe((data:any)=>{
      this.videos=data.videos
  }
  )}

  setData(){
    return new Promise((resolve, reject) => {
      this.service.upload(this.selectedVideo).subscribe((data:any)=>{
        resolve(data);
    }
    , error => reject(error));
  });
  }
  go(){
    console.log(this.selectedVideo);
    this.isLoading=true
    this.setData().then(rep=>this.router.navigate(["/keyframes"]))
    
}
    

}
