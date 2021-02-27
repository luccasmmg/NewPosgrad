import React, { FC } from 'react';
import {
  Edit,
  SimpleForm,
  TextInput,
  BooleanInput,
  NumberInput,
} from 'react-admin';

export const PosGraduationEdit: FC = (props) => (
  <Edit {...props} title="Editar Pós Graduação">
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
  </Edit>
);
