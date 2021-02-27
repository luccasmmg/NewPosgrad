export const getMessage = async (route: string) => {
  const response = await fetch(route);

  const data = await response.json();

  if (data) {
    return data;
  }

  return Promise.reject('Failed to get message from backend');
};
