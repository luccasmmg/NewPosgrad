import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  FileInput,
  FileField,
} from 'react-admin';

export const CovenantCreate: FC = (props) => (
  <Create {...props} title="Adicionar convenio">
    <SimpleForm>
      <TextInput label="Nome convênio" source="name" />
      <TextInput label="Siga convênio" source="initials" />
      <FileInput label="Siga convênio" source="logo_file" multiple={false}>
        <FileField source="src" title="title" />
      </FileInput>
    </SimpleForm>
  </Create>
);
