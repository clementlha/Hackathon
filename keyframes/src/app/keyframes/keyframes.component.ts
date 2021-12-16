import { Component, OnInit } from '@angular/core';
import { MatSlider } from '@angular/material/slider';


@Component({
  selector: 'app-keyframes',
  templateUrl: './keyframes.component.html',
  styleUrls: ['./keyframes.component.css']
})
export class KeyframesComponent implements OnInit {

  max_frames=100;

  images= [
  {'name': 'img1271.jpg',
    'start':0,
    'end':25},
  {'name':'img2542.jpg',
  'start':25,
    'end':50},
  {'name':'img3813.jpg',
    'start':50,
      'end':75},
  {'name':'img5084.jpg',
      'start':75,
        'end':100}
];
current_img=this.images[0];
  
  constructor() { }

  ngOnInit(): void {
    

  }
  showVal(val:any){
    console.log(val.value)
    for (let img of this.images){
      if(val.value>=img.start && val.value<img.end)
        {this.current_img=img;
        break;}
    }
  }

}
