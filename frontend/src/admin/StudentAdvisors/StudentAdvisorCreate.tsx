import React, { FC } from 'react';
import { Create, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const StudentAdvisorCreate: FC = (props) => (
  <Create {...props} title="Adicionar orientador de estudante">
    <SimpleForm>
      <NumberInput label="Matricula orientando" source="registration" />
      <TextInput label="Nome orientador" source="advisor_name" />
    </SimpleForm>
  </Create>
);
