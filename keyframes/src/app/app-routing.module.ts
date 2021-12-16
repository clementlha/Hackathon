import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { KeyframesComponent } from './keyframes/keyframes.component';

const routes: Routes = [
  { path: '', redirectTo: '/keyframes', pathMatch: 'full' },
  { path: 'keyframes', component: KeyframesComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
