import { TestBed } from '@angular/core/testing';

import { KeyframesService } from './keyframes.service';

describe('KeyframesService', () => {
  let service: KeyframesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KeyframesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
