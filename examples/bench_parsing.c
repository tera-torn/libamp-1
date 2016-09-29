/* Copyright (c) 2011 - Eric P. Mangold
 * Copyright (c) 2011 - Peter Le Bek
 *
 * See LICENSE.txt for details.
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>

/* libamp */
#include <amp.h>

#include "common.h"
/* strtonum() from OpenBSD */
#include "strtonum.h"


void usage()
{
    fprintf(stderr, "Usage: ./bench_parsing_new <count>\n\n");
    exit(1);
}

uint8_t packet[] = {'\x00', '\x04', '_', 'a', 's', 'k', '\x00', '\x01', '2', '\x00', '\x08', '_', 'c', 'o', 'm', 'm', 'a', 'n', 'd', '\x00', '\x17', 'R', 'e', 's', 'p', 'o', 'n', 'd', 'T', 'o', 'J', 'u', 'n', 'k', 'A', 'p', 'i', 'C', 'o', 'm', 'm', 'a', 'n', 'd', '\x00', '\x04', 'a', 'r', 'g', 's', '\x00', '\x02', '{', '}', '\x00', '\x07', 'c', 'o', 'm', 'm', 'a', 'n', 'd', '\x00', '\x05', 'h', 'e', 'l', 'l', 'o', '\x00', '\x00'};

int main(int argc, char *argv[])
{
    int ret;
    long count = 0;
    int bytesConsumed = 0;
    long limit = 0;
    AMP_Proto_T *amp;
    AMP_Box_T   *box;

    if (argc != 2)
        usage();

    limit = (long)strtonum(argv[1], 1, 1000000000, NULL);
    if (limit == 0)
        usage();

    amp = amp_new_proto();
    box = amp_new_box();

    while (count++ <= limit) {
        amp_parse_box(amp, box, &bytesConsumed, packet, sizeof(packet));
    }

    fprintf(stderr, "Done!\n");
    return 0;
}
