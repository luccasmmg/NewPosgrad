import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  NumberInput,
  BooleanInput,
  SelectInput,
} from 'react-admin';

export const ParticipationCreate: FC = (props) => (
  <Create {...props} title="Adicionar participação acadêmica">
    <SimpleForm>
      <TextInput label="Título participação" source="title" />
      <TextInput label="Descrição participação" source="description" />
      <TextInput label="Localização da participação" source="location" />
      <NumberInput label="Ano participação" source="year" />
      <BooleanInput
        label="Participação Internacional?"
        source="international"
      />
      <SelectInput
        label="Tipo de intercambio"
        source="category"
        choices={[
          { id: 'cooperation_agreement', name: 'Acordo de Cooperação' },
          { id: 'prize', name: 'Prêmio' },
          { id: 'event', name: 'Evento' },
          { id: 'parternship', name: 'Parceria' },
          { id: 'posdoc', name: 'Pos-Doutorado' },
        ]}
      />
    </SimpleForm>
  </Create>
);
