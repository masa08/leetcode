class Calculator {
  /**
   * @param {number} value
   */
  constructor(value) {
    this.value = value;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  add(value) {
    const newValue = this.value + value;
    return new Calculator(newValue);
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  subtract(value) {
    const newValue = this.value - value;
    return new Calculator(newValue);
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  multiply(value) {
    const newValue = this.value * value;
    return new Calculator(newValue);
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  divide(value) {
    if (value == 0) {
      throw 'Division by zero is not allowed';
    }
    const newValue = this.value / value;
    return new Calculator(newValue);
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  power(value) {
    const newValue = this.value ** value;
    return new Calculator(newValue);
  }

  /**
   * @return {number}
   */
  getResult() {
    return this.value;
  }
}
