import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';
import { IndexRouterComponent } from './views/index-router/index-router.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { FormComponent } from './components/form/form.component';
import { TableViewComponent } from './views/table-view/table-view.component';
import { AboutViewComponent } from './views/about-view/about-view.component';
import { TableShowViewComponent } from './views/table-show-view/table-show-view.component'

@NgModule({
  declarations: [
    AppComponent,
    IndexRouterComponent,
    HeaderComponent,
    FooterComponent,
    FormComponent,
    TableViewComponent,
    AboutViewComponent,
    TableShowViewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule // Peticiones backend
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
