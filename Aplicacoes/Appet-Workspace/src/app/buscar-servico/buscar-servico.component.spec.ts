import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BuscarServicoComponent } from './buscar-servico.component';

describe('BuscarServicoComponent', () => {
  let component: BuscarServicoComponent;
  let fixture: ComponentFixture<BuscarServicoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BuscarServicoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BuscarServicoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
