import { Component, OnInit } from '@angular/core';

@Component({
  // default selector
  selector: 'app-servers',
  // selector by attribute
  // selector:'[app-servers]',

  // selector by class
  // selector:'.app-servers',

  // use html code directly as template
  // template: `
  // <app-server></app-server>
  // <app-server></app-server>`,
  // defualt
  templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.css']
})
export class ServersComponent implements OnInit {
  allowNewServer = false;
  serverCreationStatus = 'No server was created';
  serverName = 'TestServer';
  serverCreated = false;
  servers = ['TestServer 1','TestServer 2']

  constructor() {
    setTimeout(() => {this.allowNewServer = true;}, 2000);
  }

  ngOnInit() {
  }
  onCreateServer(){
    this.serverCreated = true;
    this.servers.push(this.serverName)
    this.serverCreationStatus = "Server was created, Name is "+ this.serverName ;
  }

  onUpdateServerName(event:any){
    console.log(event);
    this.serverName = (<HTMLInputElement>event.target).value;

  }
}
