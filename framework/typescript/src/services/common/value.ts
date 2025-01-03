// This file was generated by liblab | https://liblab.com/

import { z } from 'zod';

/**
 * The shape of the model inside the application code - what the users use
 */
export const value = z.lazy(() => {
  return z.object({
    name: z.string(),
    value: z.string().optional().nullable(),
  });
});

/**
 *
 * @typedef  {Value} value
 * @property {string}
 * @property {string}
 */
export type Value = z.infer<typeof value>;

/**
 * The shape of the model mapping from the api schema into the application shape.
 * Is equal to application shape if all property names match the api schema
 */
export const valueResponse = z.lazy(() => {
  return z
    .object({
      name: z.string(),
      value: z.string().optional().nullable(),
    })
    .transform((data) => ({
      name: data['name'],
      value: data['value'],
    }));
});

/**
 * The shape of the model mapping from the application shape into the api schema.
 * Is equal to application shape if all property names match the api schema
 */
export const valueRequest = z.lazy(() => {
  return z.object({ name: z.string().nullish(), value: z.string().nullish() }).transform((data) => ({
    name: data['name'],
    value: data['value'],
  }));
});
