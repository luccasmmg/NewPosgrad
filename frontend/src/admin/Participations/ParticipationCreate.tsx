import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  NumberInput,
  BooleanInput,
} from 'react-admin';

export const ParticipationCreate: FC = (props) => (
  <Create {...props} title="Adicionar participação acadêmica">
    <SimpleForm>
      <TextInput label="Título participação" source="title" />
      <TextInput label="Descrição participação" source="description" />
      <NumberInput label="Ano participação" source="year" />
      <BooleanInput
        label="Participação Internacional?"
        source="international"
      />
    </SimpleForm>
  </Create>
);
