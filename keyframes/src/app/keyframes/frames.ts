export class frames{
    nom_video?:string;
    nb_frames?:number;
    frames?:any[];

    constructor(video:string,nb_frames:number,frames:any[]){
        this.nom_video=video;
        this.nb_frames=nb_frames;
        this.frames=frames;

    }

}