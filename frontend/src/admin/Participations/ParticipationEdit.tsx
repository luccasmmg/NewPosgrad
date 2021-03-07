import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  BooleanInput,
  TextInput,
  NumberInput,
} from 'react-admin';

export const ParticipationEdit: FC = (props) => (
  <Edit {...props} title="Editar participações">
    <SimpleForm>
      <TextInput label="Título participação" source="title" />
      <TextInput label="Descrição participação" source="description" />
      <NumberInput label="Ano participação" source="year" />
      <BooleanInput
        label="Participação Internacional?"
        source="international"
      />
    </SimpleForm>
  </Edit>
);
