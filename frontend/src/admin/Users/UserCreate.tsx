import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  PasswordInput,
  BooleanInput,
  NumberInput,
} from 'react-admin';

export const UserCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput label="Email" source="email" />
      <TextInput label="Primeiro Nome" source="first_name" />
      <TextInput label="Sobrenome" source="last_name" />
      <NumberInput label="Id do grupo" source="owner_id" step={1} />
      <PasswordInput source="password" />
      <BooleanInput label="É superusuário?" source="is_superuser" />
      <BooleanInput label="É ativo?" source="is_active" />
    </SimpleForm>
  </Create>
);
