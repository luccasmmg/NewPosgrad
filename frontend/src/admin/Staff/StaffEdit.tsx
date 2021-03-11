import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput, SelectInput } from 'react-admin';

export const StaffEdit: FC = (props) => (
  <Edit {...props} title="Editar membro de equipe">
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
    </SimpleForm>
  </Edit>
);
