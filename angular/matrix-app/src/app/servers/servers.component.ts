import { Component, OnInit } from '@angular/core';

@Component({
  // default selector
  selector: 'app-servers',
  // selector by attribute
  // selector:'[app-servers]',

  // selector by class
  // selector:'.app-servers',

  // use html code directly as template
  template: `
  <app-server></app-server>
  <app-server></app-server>`,
  // defualt
  // templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.css']
})
export class ServersComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
