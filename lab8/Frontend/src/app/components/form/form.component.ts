import { Component, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Employee } from 'src/app/interfaces/Employee';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent {
  @Input() title !: string
  @Input() title_button !: string
  @Output() submitData = new EventEmitter<Employee>()

  formData = new FormGroup({
    firstName: new FormControl('', [Validators.minLength(25), Validators.required]),
    lastName: new FormControl('', [Validators.minLength(25), Validators.required]),
    age: new FormControl('', [Validators.required, Validators.min(18)]),
    salary: new FormControl('', [Validators.required, Validators.min(100)])
  })

  submit() : void {
    this.submitData.emit(this.formData.value as Employee)
  }

}
