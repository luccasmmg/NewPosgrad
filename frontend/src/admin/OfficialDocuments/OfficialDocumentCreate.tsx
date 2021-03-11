import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  FileInput,
  FileField,
  SelectInput,
} from 'react-admin';

export const OfficialDocumentCreate: FC = (props) => (
  <Create {...props} title="Adicionar documento oficial">
    <SimpleForm>
      <TextInput label="Título" source="title" />
      <TextInput label="Código" source="cod" />
      <SelectInput
        label="Tipo de documento"
        source="category"
        choices={[
          { id: 'regiments', name: 'Regimento' },
          { id: 'records', name: 'ATA' },
          { id: 'resolutions', name: 'Resolução' },
          { id: 'plans', name: 'Plano' },
          { id: 'others', name: 'Outro' },
        ]}
      />
      <FileInput label="Arquivo" source="file" multiple={false}>
        <FileField source="src" title="title" />
      </FileInput>
    </SimpleForm>
  </Create>
);
