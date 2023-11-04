import * as jwt_decode from 'jwt-decode';

export function decodeToken(token) {
  try {
    const decoded = jwt_decode(token);
    return decoded;
  } catch (error) {
    return null;
  }
}
