// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  EditButton,
  FileField,
  SelectField,
} from 'react-admin';

export const OfficialDocumentList: FC = (props) => (
  <List {...props} title="Listar convênios">
    <Datagrid>
      <FileField label="Arquivo" title="Baixe aqui" source="file" />
      <TextField label="Título" source="title" />
      <TextField label="Código" source="cod" />
      <SelectField
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
      <EditButton />
    </Datagrid>
  </List>
);
