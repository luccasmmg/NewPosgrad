import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput } from 'react-admin';

export const StudentAdvisorEdit: FC = (props) => (
  <Edit {...props} title="Editar orientador">
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput label="Matricula orientando" source="registration" />
      <TextInput label="Nome orientador" source="advisor_name" />
    </SimpleForm>
  </Edit>
);
