import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  FileInput,
  FileField,
} from 'react-admin';
import RichTextInput from 'ra-input-rich-text';

export const CovenantCreate: FC = (props) => (
  <Create {...props} title="Adicionar convenio">
    <SimpleForm>
      <TextInput label="Nome convênio" source="name" />
      <TextInput label="Siga convênio" source="initials" />
      <RichTextInput label="Objeto" source="object" />
      <FileInput label="Siga convênio" source="logo_file" multiple={false}>
        <FileField source="src" title="title" />
      </FileInput>
    </SimpleForm>
  </Create>
);
