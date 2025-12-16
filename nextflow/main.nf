#!/usr/bin/env nextflow
include {train_predict} from './modules/train_predict'
include {aggregate} from './modules/aggregate'

workflow {
    main:
    ch_inputs = channel.fromPath(params.input)
            .splitCsv( header: true )
            .map {
                row -> [lon:row.LON, lat:row.LAT, seed:row.SEED]
            }

    train_predict(ch_inputs)

    trained = train_predict.out
        .collect()

    best = aggregate(trained)

    publish:
    c = best
}

output {
    c {
        path 'output'
    }
}
