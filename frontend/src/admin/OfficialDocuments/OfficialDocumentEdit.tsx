import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, SelectInput } from 'react-admin';

export const OfficialDocumentEdit: FC = (props) => (
  <Edit {...props} title="Editar documento oficial">
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
    </SimpleForm>
  </Edit>
);
