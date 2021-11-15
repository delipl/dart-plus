import { Base64 } from 'js-base64';
export function encrypt_password(password){
    return Base64.encode(password)
}