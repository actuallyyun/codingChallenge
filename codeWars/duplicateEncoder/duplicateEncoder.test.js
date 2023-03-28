import { describe, expect, test } from '@jest/globals'
import { duplicateEncode1, duplicateEncode2 } from './duplicateEncoder'

describe('test duplicateEncode1', () => {
  test('din=>(((', () => {
    const word = 'din'
    const result = '((('
    expect(duplicateEncode1(word)).toStrictEqual(result)
  })

  test('recede=>()()()', () => {
    const word = 'recede'
    const result = '()()()'
    expect(duplicateEncode1(word)).toStrictEqual(result)
  })
  test('Success=>)())())', () => {
    const word = 'Success'
    const result = ')())())'
    expect(duplicateEncode1(word)).toStrictEqual(result)
  })
  test('(( @=>))((', () => {
    const word = '(( @'
    const result = '))(('
    expect(duplicateEncode1(word)).toStrictEqual(result)
  })
})

describe('test duplicateEncode2', () => {
  test('din=>(((', () => {
    const word = 'din'
    const result = '((('
    expect(duplicateEncode2(word)).toStrictEqual(result)
  })

  test('recede=>()()()', () => {
    const word = 'recede'
    const result = '()()()'
    expect(duplicateEncode2(word)).toStrictEqual(result)
  })
  test('Success=>)())())', () => {
    const word = 'Success'
    const result = ')())())'
    expect(duplicateEncode2(word)).toStrictEqual(result)
  })
  test('(( @=>))((', () => {
    const word = '(( @'
    const result = '))(('
    expect(duplicateEncode2(word)).toStrictEqual(result)
  })
})
