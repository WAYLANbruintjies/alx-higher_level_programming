#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  let listLen = list.length -1;

  while ((listLen - 1) > 0) {
    const temp = list[listLen];
    list[listLen] = list[i];
    list[i] = temp;
    i++;
    listLen--;
  }
  return list;
};
