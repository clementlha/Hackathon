import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { KeyframesComponent } from './keyframes/keyframes.component';
import { AcceuilComponent } from './acceuil/acceuil.component';

const routes: Routes = [
  { path: '', redirectTo: '/accueil', pathMatch: 'full' },
  { path: 'keyframes', component: KeyframesComponent },
  { path: 'accueil', component: AcceuilComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
