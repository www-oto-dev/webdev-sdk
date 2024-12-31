// This file was generated by liblab | https://liblab.com/

import { z } from 'zod';

/**
 * The shape of the model inside the application code - what the users use
 */
export const formula = z.lazy(() => {
  return z.object({
    name: z.string(),
    value: z.string().optional().nullable(),
    form: z.string().optional().nullable(),
    engine: z.string().optional().nullable(),
  });
});

/**
 *
 * @typedef  {Formula} formula
 * @property {string}
 * @property {string}
 * @property {string}
 * @property {string}
 */
export type Formula = z.infer<typeof formula>;

/**
 * The shape of the model mapping from the api schema into the application shape.
 * Is equal to application shape if all property names match the api schema
 */
export const formulaResponse = z.lazy(() => {
  return z
    .object({
      name: z.string(),
      value: z.string().optional().nullable(),
      form: z.string().optional().nullable(),
      engine: z.string().optional().nullable(),
    })
    .transform((data) => ({
      name: data['name'],
      value: data['value'],
      form: data['form'],
      engine: data['engine'],
    }));
});

/**
 * The shape of the model mapping from the application shape into the api schema.
 * Is equal to application shape if all property names match the api schema
 */
export const formulaRequest = z.lazy(() => {
  return z
    .object({
      name: z.string().nullish(),
      value: z.string().nullish(),
      form: z.string().nullish(),
      engine: z.string().nullish(),
    })
    .transform((data) => ({
      name: data['name'],
      value: data['value'],
      form: data['form'],
      engine: data['engine'],
    }));
});