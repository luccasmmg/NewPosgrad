import React, { FC } from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  BooleanInput,
  NumberInput,
} from 'react-admin';

export const PosGraduationCreate: FC = (props) => (
  <Create {...props} title="Criar Pós Graduação">
    <SimpleForm>
      <NumberInput label="Código no Sigaa" source="sigaa_code" />
      <NumberInput label="ID Unidade" source="id_unit" />
      <TextInput label="Iniciais" source="initials" />
      <TextInput label="Nome" source="name" />
      <TextInput
        type="text"
        label="Descrição grande"
        source="description_big"
      />
      <TextInput
        type="text"
        label="Descrição pequena"
        source="description_small"
      />
      <TextInput label="URL Antiga" type="url" source="old_url" />
      <BooleanInput label="Cadastrado?" source="is_signed_in" />
    </SimpleForm>
  </Create>
);
