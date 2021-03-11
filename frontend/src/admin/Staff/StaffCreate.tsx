import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  FileInput,
  FileField,
  SelectInput,
} from 'react-admin';

export const StaffCreate: FC = (props) => (
  <Create {...props} title="Adicionar membro da equipe">
    <SimpleForm>
      <TextInput label="Nome membro" source="name" />
      <TextInput label="Descrição" source="description" />
      <SelectInput
        label="Tipo de membro"
        source="rank"
        choices={[
          { id: 'coordinator', name: 'Coordenador' },
          { id: 'vice_coordinator', name: 'Vice-Coordenador' },
          { id: 'secretariat', name: 'Secretário' },
          { id: 'intern', name: 'Bolsista' },
        ]}
      />
      <FileInput label="Foto do membro" source="photo" multiple={false}>
        <FileField source="src" title="title" />
      </FileInput>
    </SimpleForm>
  </Create>
);
