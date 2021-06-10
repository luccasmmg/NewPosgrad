// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  BooleanField,
  SelectField,
  EditButton,
} from 'react-admin';

export const ParticipationList: FC = (props) => (
  <List {...props} title="Listar participações">
    <Datagrid>
      <TextField label="Título participação" source="title" />
      <TextField label="Descrição participação" source="description" />
      <TextField label="Localização da participação" source="location" />
      <TextField label="Ano participação" source="year" />
      <BooleanField
        label="Participação Internacional?"
        source="international"
      />
      <SelectField
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
      <EditButton />
    </Datagrid>
  </List>
);
