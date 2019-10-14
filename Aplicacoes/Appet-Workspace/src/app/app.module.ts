import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import { MenuPrincipalComponent } from './menu-principal/menu-principal.component';
import { RodapeComponent } from './rodape/rodape.component';
import { LoginComponent } from './login/login.component';
import { NovoUsuarioComponent } from './novo-usuario/novo-usuario.component';
import { BuscarServicoComponent } from './buscar-servico/buscar-servico.component';

@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    MenuPrincipalComponent,
    RodapeComponent,
    LoginComponent,
    NovoUsuarioComponent,
    BuscarServicoComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
