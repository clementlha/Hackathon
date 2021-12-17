import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatSliderModule } from '@angular/material/slider';
import { MatCardModule} from '@angular/material/card';  
import { HttpClientModule } from '@angular/common/http';
import {MatInputModule} from '@angular/material/input';
import {FormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { KeyframesComponent } from './keyframes/keyframes.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AcceuilComponent } from './acceuil/acceuil.component';
import { MatSelectModule } from '@angular/material/select';
import{MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';


@NgModule({
  declarations: [
    AppComponent,
    KeyframesComponent,
    AcceuilComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatCardModule,
    HttpClientModule,
    MatInputModule,
    FormsModule,
    MatSelectModule,
    MatButtonModule,
    MatIconModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
