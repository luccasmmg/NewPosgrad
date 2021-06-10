import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  BooleanInput,
  TextInput,
  NumberInput,
  SelectInput,
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
  </Edit>
);
