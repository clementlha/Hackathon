import { ifStmt } from '@angular/compiler/src/output/output_ast';
import { Component, OnInit } from '@angular/core';
import {frames} from './frames';
import { KeyframesService } from './keyframes.service';


@Component({
  selector: 'app-keyframes',
  templateUrl: './keyframes.component.html',
  styleUrls: ['./keyframes.component.css']
})
export class KeyframesComponent implements OnInit {

frames?:frames;
current_image?:any;
slider_val=0;

playing:Boolean=false
playing_val="play_arrow"
  
  constructor(private service: KeyframesService) {
    
    }

  ngOnInit(): void {
    this.service.getFrames().subscribe((data:any)=>{
      console.log(data)
      var nb_frame=data.nb_frames
      var nom_video=data.nom_video
      var img=data.frames
      this.frames=new frames(nom_video,nb_frame,img); 
      console.log(this.frames!)
      this.current_image=this.frames!.frames![0];
      
    })

  }
  set_img(){
    for (let img of this.frames!.frames!){
      if(this.slider_val>=img.debut && this.slider_val<img.fin)
        {this.current_image=img;
        break;}
    }

  }
  showVal(val:any){
    this.slider_val=val.value
    this.set_img()
  }
  go(val:any){
    this.slider_val=val.debut;
    this.set_img();
    
}
delay(ms: number) {
  return new Promise( resolve => setTimeout(resolve, ms) );
}
tooglePlaying(){
  this.playing=!this.playing;
  if(this.playing)
    this.playing_val="pause"
  else
    this.playing_val="play_arrow"

}
async play(){
  this.tooglePlaying()
  for(let f of this.frames!.frames!)
    {if (f.debut<=this.current_image!.debut)
      continue
      if (this.playing==false)
        break;
      this.go(f)
      await this.delay(1000);
  }
}


}
